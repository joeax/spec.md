const express = require('express');
const tasksRouter = require('./routes/tasks');

const app = express();
app.use(express.json());
app.use('/tasks', tasksRouter);

const port = process.env.PORT || 3000;
app.listen(port, () => {
  console.log(`Task Tracker API listening on port ${port}`);
});

module.exports = app;
