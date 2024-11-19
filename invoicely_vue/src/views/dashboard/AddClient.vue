<template>
  <div class="page-add-client">
    <div class="container">
      <nav class="breadcrumb">
        <ul class="breadcrumb-list">
          <li><router-link to="/dashboard" class="breadcrumb-link">Dashboard</router-link></li>
          <li><router-link to="/dashboard/clients" class="breadcrumb-link">Clients</router-link></li>
          <li class="breadcrumb-link is-active"><router-link to="/dashboard/clients/add">Add</router-link></li>
        </ul>
      </nav>
      <div class="colums">
        <div class="colum">
          <h1 class="title">Add client</h1>
        </div>
        <div class="fields">
          <div class="field">
            <label for="field-label">Name</label>
            <input type="text" name="name" class="field-input" v-model="client.name">
          </div>
          <div class="field">
            <label for="field-label">Email</label>
            <input type="email" name="email" class="field-input" v-model="client.email">
          </div>
          <div class="field">
            <label for="field-label">Address 1</label>
            <input type="text" name="address1" class="field-input" v-model="client.address1">
          </div>
          <div class="field">
            <label for="field-label">Address 2</label>
            <input type="email" name="address2" class="field-input" v-model="client.address2">
          </div>
        </div>
        <div class="fields">
          <div class="field">
            <label for="field-label">Zipcode</label>
            <input type="text" name="zipcode" class="field-input" v-model="client.zipcode">
          </div>
          <div class="field">
            <label for="field-label">Place</label>
            <input type="email" name="place" class="field-input" v-model="client.place">
          </div>
          <div class="field">
            <label for="field-label">Country</label>
            <input type="text" name="country" class="field-input" v-model="client.country">
          </div>
        </div>
        <div class="buttons">
          <button class="button" @click="submitForm">Submit</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'AddClient',
  data() {
    return {
      client: {}
    }
  },
  methods: {
    submitForm() {
      axios
        .post("/api/v1/clients/", this.client)
        .then(response => {
          this.$router.push('/dashboard/clients')
        })
        .catch(error => {
          console.log(JSON.stringify(error))
        })
    }
  }

}
</script>

<style lang="scss" scoped>
@import "@/assets/styles/fomrs.scss";
.page-add-client {
  .colums {
    .colum {
      .title {
        padding: 10px 0;
      }
    }
    .buttons {
      padding: 20px 0;
      .button {
        background-color: #4CAF50;
        font-weight: 600;
        color: #fff;
      }
    }
  }
}
</style>