document.getElementById("directory-select").addEventListener("click", ()=>{directory_select()}, false);

function directory_select() {
  eel.select_directory();
}

eel.expose(receive_path);
function receive_path(dir_path) {
  alert(dir_path);
}

eel.expose(warning);
function warning(msg) {
  alert(msg)
}