<template>
  <div>
    <form @submit.prevent="submitForm">
      <div class="row g-2">
        <div class="col-12">
          <label for="name">Name:</label>
          <input class="input-group" type="text" id="name" v-model="name" />
        </div>
        <div class="col-12">
          <label for="age">Age:</label>
          <input class="input-group" type="number" id="age" v-model.number="age" />
        </div>
        <div class="col-12">
          <button class="btn btn-primary" type="submit">Submit</button>
        </div>
      </div>
    </form>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      name: '',
      age: null,
    };
  },
  methods: {
    submitForm() {
      axios.post('http://127.0.0.1:8000/api/v1/form/', {
        name: this.name,
        age: this.age,
      })
        .then(response => {
          console.log(response.data);
          this.name = '';
          this.age = null;
        })
        .catch(error => {
          console.log(error.response.data);
        });
    },
  },
};
</script>