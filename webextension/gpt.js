function onCreated() {
  if (browser.runtime.lastError) {
    console.log(`Error: ${browser.runtime.lastError}`);
  } else {
    console.log("Item created successfully");
  }
}

browser.menus.create({
  id: "search",
  title: "GPT",
  contexts: ["selection"]
}, onCreated);

browser.menus.onClicked.addListener((info, tab) => {
  if (info.menuItemId === "search") {
    const query = encodeURIComponent(info.selectionText);
    const url = `http://localhost:8501/?q=${query}`;
    browser.tabs.create({ url: url });
  }
});
