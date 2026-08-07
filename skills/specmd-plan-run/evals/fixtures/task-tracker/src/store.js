const { createTask } = require('./models/task');

const tasks = new Map();

function list() {
  return Array.from(tasks.values());
}

function get(id) {
  return tasks.get(id);
}

function create(title) {
  const task = createTask({ title });
  tasks.set(task.id, task);
  return task;
}

function update(id, changes) {
  const task = tasks.get(id);
  if (!task) return undefined;
  Object.assign(task, changes);
  return task;
}

function remove(id) {
  return tasks.delete(id);
}

module.exports = { list, get, create, update, remove };
