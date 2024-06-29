const express = require('express');
const app = express();
const port = 8000;

app.use(express.static('public'));

app.post('/upload', (req, res) => {
    // 處理上傳的文件
    res.send({ message: 'File uploaded successfully.' });
});

app.listen(port, () => {
    console.log(`Server is running on http://localhost:${port}`);
});
