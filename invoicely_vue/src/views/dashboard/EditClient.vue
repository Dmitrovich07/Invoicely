<template>
  <div class="page-edit-client">
    <div class="container">
      <nav class="breadcrumb">
        <ul class="breadcrumb-list">
          <li><router-link to="/dashboard" class="breadcrumb-link">Dashboard</router-link></li>
          <li><router-link to="/dashboard/clients" class="breadcrumb-link">Clients</router-link></li>
          <li><router-link :to="{ name: 'Client', params: { id: client.id } }" class="breadcrumb-link">{{ client.name }}</router-link></li>
          <li class="breadcrumb-link is-active"><router-link :to="{ name: 'EditClient', params: { id: client.id } }">Edit</router-link></li>
        </ul>
      </nav>
      <div class="columns">
        <div class="column">
          <h1 class="title">Edit {{ client.name }}</h1>
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
          <button class="button" @click="submitForm">Save changes</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'EditClient',
  data() {
    return {
      client: {}
    }
  },
  mounted() {
    this.getClient()
  },
  methods: {
    getClient() {
      const clientID = this.$route.params.id

      axios
        .get(`/api/v1/clients/${clientID}`)
        .then(response => {
          this.client = response.data
        })
        .catch(error => {
          console.log(JSON.stringify(error))
        })
    },
    submitForm() {
      const clientID = this.$route.params.id
      axios
        .patch(`/api/v1/clients/${clientID}/`, this.client)
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

.page-edit-client {
  .container {
    .columns {
      .column {
        .title {
          padding: 10px 0;
        }
      }
      .buttons {
        padding: 10px 0;
        .button {
          background-color: #4CAF50;
          color: #fff;
        }
      }
    }
  }
}
</style>