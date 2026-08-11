let nextId = 1;

function createTask({ title }) {
  return {
    id: String(nextId++),
    title,
    completed: false,
    createdAt: new Date().toISOString(),
  };
}

module.exports = { createTask };
