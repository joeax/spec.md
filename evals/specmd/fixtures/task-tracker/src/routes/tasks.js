const express = require('express');
const store = require('../store');

const router = express.Router();

router.get('/', (req, res) => {
  res.json(store.list());
});

router.post('/', (req, res) => {
  const task = store.create(req.body.title);
  res.status(201).json(task);
});

router.get('/:id', (req, res) => {
  const task = store.get(req.params.id);
  if (!task) return res.sendStatus(404);
  res.json(task);
});

router.put('/:id', (req, res) => {
  const task = store.update(req.params.id, req.body);
  if (!task) return res.sendStatus(404);
  res.json(task);
});

router.delete('/:id', (req, res) => {
  const removed = store.remove(req.params.id);
  if (!removed) return res.sendStatus(404);
  res.sendStatus(204);
});

// Not yet documented in SPEC.md's API section.
router.patch('/:id/complete', (req, res) => {
  const task = store.complete(req.params.id);
  if (!task) return res.sendStatus(404);
  res.json(task);
});

module.exports = router;
