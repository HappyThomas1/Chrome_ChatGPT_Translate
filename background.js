// メニューアイテムの作成
const contextMenuItems = [
    { id: 'Translate_Text_ChatGPT', title: 'Translate by ChatGPT' },
    { id: 'Translate_Text_DEEPL', title: 'Translate by DeepL' },
    { id: 'Explain_Code_GPT4', title: 'Code explanation' },
];
  
contextMenuItems.forEach(item => {
    // メニューアイテムがすでに存在するかどうか確認
    chrome.contextMenus.remove(item.id, function() {
        // 削除した後、新たに作成
        chrome.contextMenus.create({
            id: item.id,
            title: item.title,
            contexts: ['selection'],
        });
    });
});

let latestResult = ''; // 最新の結果を更新

// メニューアイテムがクリックされたときのリスナー
chrome.contextMenus.onClicked.addListener(function(info, tab) {
    let processMode;
    if (info.menuItemId === 'Translate_Text_ChatGPT') {
        processMode = "ChatGPT";
    } else if (info.menuItemId === 'Translate_Text_DEEPL') {
        processMode = "DeepL";
    } else if (info.menuItemId === 'Explain_Code_GPT4') {
        processMode = "CodeExplain";
    } else {
        return;
    }
    const selectedText = info.selectionText;
    fetch('http://localhost:8000/process_text', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({text: selectedText, mode: processMode}),
    })
    .then(response => response.json())
    .then(data => {
        // 最新の結果を更新
        latestResult = data.result;
        
        // 新しいウィンドウを作成
        chrome.windows.create({
            url: chrome.runtime.getURL("popup.html"),
            type: "popup",
            width: 500,
            height: 200,
        }, function(window) {
            chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
                if (message.from === 'popup' && message.subject === 'loadData') {
                    sendResponse({ text: latestResult });
                }
        });
    });
});


});
  
  
  
  
  