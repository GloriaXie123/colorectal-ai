const backendUrl = window.location.origin + '/recommend';

document.getElementById('submitButton').addEventListener('click', function() {
    const patientId = document.getElementById('patientIdInput').value;
    const ctDNA = parseFloat(document.getElementById('ctDNAInput').value);

    if (!patientId || isNaN(ctDNA)) {
        alert('请填写完整信息');
        return;
    }

    fetch(backendUrl, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        },
        body: JSON.stringify({
            patient_id: patientId,
            ctDNA: parseFloat(ctDNA)
        })
    })
    .then(response => response.json())
    .then(data => {
        const recommendationOutput = document.getElementById('recommendationOutput');
        const recommendation = data.recommendation;

        // 清空之前的内容
        recommendationOutput.innerHTML = '';

        if (recommendation && typeof recommendation === 'object') {
            // 遍历 recommendation 里的每一条
            for (const [key, value] of Object.entries(recommendation)) {
                const item = document.createElement('div');
                item.innerHTML = `<strong>${key}:</strong> ${value}`;
                recommendationOutput.appendChild(item);
            }
        } else {
            recommendationOutput.innerText = '暂无推荐内容。';
        }
    })
    .catch(error => {
        console.error('请求失败:', error);
        document.getElementById('recommendationOutput').innerText = '请求失败，请稍后重试。';
    });
});

