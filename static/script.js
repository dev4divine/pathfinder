// Initialize CodeMirror editor
const editor = CodeMirror.fromTextArea(document.getElementById('jsonData'), {
    lineNumbers: true,
    mode: 'application/json',
    theme: 'material',
    indentUnit: 4,
    smartIndent: true,
    lineWrapping: true,
    autofocus: true,
});
// Function to validate JSON data
function isValidJson(jsonData) {
    if (!jsonData.trim()) {
        // If JSON data is empty, return false
        return false;
    }
    try {
        JSON.parse(jsonData);
        // If parsing successful, return true
        return true;
    } catch (error) {
        // If parsing failed, return false
        return false;
    }
}

// Add event listener for changes in the editor
editor.on('change', function() {
    const jsonData = editor.getValue();
    const validationResult = document.getElementById('validationResult');
    if (isValidJson(jsonData)) {
        // If JSON data is valid, display success message
        validationResult.textContent = 'JSON is valid.';
        validationResult.classList.remove('error');
    } else {
        // If JSON data is not valid, display error message
        validationResult.textContent = 'JSON is not valid.';
        validationResult.classList.add('error');
    }
});




// // Initialize JSON Editor
// const container = document.getElementById('jsoneditor');
// const options = {};
// const editor = new JSONEditor(container, options);

// // Add event listener for input changes in the textarea
// document.getElementById('jsonData').addEventListener('input', function() {
//     const jsonData = this.value.trim();
//     // Validate JSON syntax
//     try {
//         const parsedData = JSON.parse(jsonData);
//         // If parsing successful, set JSON data in the editor
//         editor.set(parsedData);
//         document.getElementById('validationResult').textContent = 'JSON is valid.';
//         document.getElementById('validationResult').classList.remove('error');
//     } catch (error) {
//         // If parsing failed, display error message
//         document.getElementById('validationResult').textContent = 'JSON is not valid: ' + error.message;
//         document.getElementById('validationResult').classList.add('error');
//     }
// });
