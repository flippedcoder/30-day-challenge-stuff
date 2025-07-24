class HashTable {
  _size;
  _table;

  constructor(size) {
    this._size = 0;
    this._table = new Array(size);
  }

  _hash(key) {
    let hash = 0;
    const keyString = String(key);

    for (let i = 0; i < keyString.length; i++) {
      hash += keyString.charCodeAt(i);
    }

    return hash % this._table.length;
  }

  set(key, value) {
    const index = this._hash(key);

    if (this._table[index]) {
      for (let i = 0; i < this._table[index].length; i++) {
        if (this._table[index][i][0] === key) {
          this._table[index][i][1] === value;

          return;
        }
      }

      this._table[index].push([key, value]);
    } else {
      this._table[index] = [];

      this._table[index].push([key, value]);
    }

    this._size++;
  }

  get(key) {
    const index = this._hash(key);

    if (this._table[index]) {
      for (let i = 0; i < this._table.length; i++) {
        if (this._table[index][i][0] === key) {
          return this._table[index][i][1];
        }
      }
    }

    return undefined;
  }

  remove(key) {
    const index = this._hash(key);

    if (this._table[index] && this._table[index].length) {
      for (let i = 0; i < this._table.length; i++) {
        if (this._table[index][i][0] === key) {
          this._table[index].splice(i, 1);

          this._size--;

          return true;
        }
      }
    } else {
      return false;
    }
  }

  display() {
    this._table.forEach((values, index) => {
      const chainedValues = values.map(([key, value]) => `[${key}: ${value}]`);

      console.log(`${index}: ${chainedValues}`);
    });
  }
}

const hashtable = new HashTable(127);

hashtable.set('Tony', 111);
hashtable.set('Tone', 150);
hashtable.set('Toni', 192);

hashtable.display();

hashtable.remove('Tone');
hashtable.display();
