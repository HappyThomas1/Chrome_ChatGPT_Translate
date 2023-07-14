window.onload = function() {
    chrome.runtime.sendMessage({from: 'popup', subject: 'loadData'}, function(response) {
        document.getElementById('result-text').innerText = response.text;
    });
};
