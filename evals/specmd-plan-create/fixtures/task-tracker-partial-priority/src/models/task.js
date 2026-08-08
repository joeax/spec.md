let nextId = 1;

function createTask({ title, priority = 'normal' }) {
  return {
    id: String(nextId++),
    title,
    priority,
    completed: false,
    createdAt: new Date().toISOString(),
  };
}

module.exports = { createTask };
