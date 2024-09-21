document.getElementById('uploadInput').addEventListener('change', function(){
    const thumbnailContainer = document.getElementById('thumbnailContainer');

    thumbnailContainer.innerHTML = '';

    [...this.files].forEach(file => {
        const fileReader = new fileReader();
        fileReader.onLoad = function(e){
            const img = document.createElement('img');
            img.src = e.target.result;
            thumbnailContainer.appendChild('img');
        }

        if(file.type.startsWith('image/')){
            fileReader.readAsDataUrl(file);
        }else{
            const'
        }
    })
})

async function upload() {
    const fileInput = document.getElementById("uploadInput");
    const fileLabel = document.getElementById("fileLabel");
    const uploadButton = document.getElementById("uploadButton");
    const progressElement = document.getElementById("uploadProgress");
    const loader = document.getElementById("loader");
    const notification = document.getElementById("notification");
    

    fileInput.disabled = true;
    fileLabel.style.pointerEvents = 'none';
    fileLabel.setAttribute('disabled', true);
    uploadButton.disabled = true;

    loader.style.display = 'block'

    progressElement.hidden = false;
    notification.style.display = 'none'

    const su = new SmashUploader({ region: "us-east-1", token: "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6ImEzM2UxMDc4LTgwMGUtNGE4MS1hOGFhLTMyMDlmZGI5Nzc3MS1ldSIsInVzZXJuYW1lIjoiNTI2MTIwMWUtNjBmYS00OGI0LTk0ZTQtMzA3ODZmNzMwOTdiIiwicmVnaW9uIjoidXMtZWFzdC0xIiwiaXAiOiIyODA0OjdmNzplMDgwOjliMzY6MmMzZTpiMTZjOjUzM2E6ZDEyMCIsInNjb3BlIjoiTm9uZSIsImFjY291bnQiOiIxZjc4Mjg5Ny05ZDc2LTQyZjgtYmY4MC1iMmVlMzJkZThmMjQtZWEiLCJpYXQiOjE3MjY5NTM4OTIsImV4cCI6NDg4MjcxMzg5Mn0.QlX14V_Nsg2engwQeXthDtYvqEmHox6R420qfAygBMc.eyJpZCI6IjYwZDVmZjUzLWM0NmEtNDEwOS05OTA2LWEzMjk3NTVjYWZiZS1ldSIsInVzZXJuYW1lIjoiNzM0YmUyNDYtNTU0ZC00N2FkLWFlYmEtYjdhNTRlN2ZhNTY3IiwicmVnaW9uIjoidXMtZWFzdC0xIiwiaXAiOiIyODA0OjdmNzplMDgwOjliMzY6N2RkMjpjZWEyOjY2ZTE6OWM1MyIsInNjb3BlIjoiTm9uZSIsImFjY291bnQiOiIxNGQyN2MyOC02Yjc5LTQyMzQtYWQyYy0xYjQyNGVjMTcwMzAtZWEiLCJpYXQiOjE3MjY5NTI2MjUsImV4cCI6NDg4MjcxMjYyNX0.rthcWbR-5klj_DNAbqk5aWBsObVXRs9BLZTXr2I4R4U" })

    try {
        const transfer = await su.upload({ files: [...fileInput.files] });
        console.log("Transfer", transfer);
        progressElement.value = 100;

        notification.textContent = 'Upload concluido com sucesso!';
        notification.className = 'notification success';
        notification.style.display = 'block';
    } catch(error) {
        console.log("Erro: ", error);
        progressElement.hidden = true;

        notification.textContent = 'Upload falhou!';
        notification.className = 'notification error';
        notification.style.display = 'block';
    } finally {
        fileInput.disabled = false;
        fileLabel.style.pointerEvents = 'auto';
        fileLabel.removeAttribute('disabled');
        uploadButton.disabled = false;

        loader.style.display = 'none';
    }

    su.on('progress', (event) => {
        const progressData = event.data && event.data.progress;

        if (progressData && progressData.percent !== undefined) {
            progressElement.value = progressData.percent;
            console.log("Progresso: ", progressData.percent);
        } else {
            console.log("Progress data esta como undefined ou o 'percent'");
        }
    });
 }