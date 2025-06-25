from typing import List

import model

class StorageException(Exception):
    pass

class LocalStorage:
    def __init__(self):
        self._id_counter = 0
        self._storage = {}
        self._date_locer = []

    def create(self, note: model.Note) -> str:
        if note.date in self._date_locer:
            raise StorageException(f"Date {note.date} is locked")
        self._id_counter += 1
        self._date_locer.append(note.date)
        note.id = str(self._id_counter)
        self._storage[note.id] = note
        return note.id

    def list(self) -> List[model.Note]:
        return list(self._storage.values())

    def read(self, _id: str) -> model.Note:
        if _id not in self._storage:
            raise StorageException(f"{_id} not found in storage")
        return self._storage[_id]

    def update(self, _id: str, note: model.Note):
        if _id not in self._storage:
            raise StorageException(f"{_id} not found in storage")
        self._date_locer.remove(self._storage[_id].date)
        note.id = _id
        self._storage[note.id] = note
        self._date_locer.append(note.date)

    def delete(self, _id: str):
        if _id not in self._storage:
            raise StorageException(f"{_id} not found in storage")
        self._date_locer.remove(self._storage[_id].date)
        del self._storage[_id]
