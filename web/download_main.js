function get_data() {
    var link = document.getElementById("link").value;
    if (document.getElementById("mp3").checked) {
        var vid_type = "mp3"
    } else {
        var vid_type = "mp4"
    }

    eel.get_data_py(link, vid_type)
    document.getElementById("download-btn").disabled = true;
    var link = document.getElementById("link").value = "";
}

eel.expose(enable_btn);
function enable_btn() {
    document.getElementById("download-btn").disabled = false;
}
