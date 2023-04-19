<template>
  <div>
    <form @submit.prevent="submitForm">
      <label for="name">Name:</label>
      <input type="text" id="name" v-model="name" />
      <label for="age">Age:</label>
      <input type="number" id="age" v-model.number="age" />
      <button type="submit">Submit</button>
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
      axios.post('http://localhost:8000/api/v1/form/', {
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
