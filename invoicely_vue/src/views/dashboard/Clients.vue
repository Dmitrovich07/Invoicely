<template>
  <div class="page-clients">
    <div class="container">
      <nav class="breadcrumb">
        <ul class="breadcrumb-list">
          <li><router-link to="/dashboard" class="breadcrumb-link">Dashboard</router-link></li>
          <li class="breadcrumb-link is-active"><router-link to="/dashboard/clients">Clients</router-link></li>
        </ul>
      </nav>
      <div class="columns">
        <div class="column">
          <h1 class="title">Clients</h1>
          <router-link :to="{ name: 'AddClient' }" class="button">Add client</router-link>
        </div>
      </div>
      <div class="clients-list">
        <div
          class="client-card"
          v-for="client in clients"
          v-bind:key="client.id"
        >
          <div class="client-img"></div>
          <div class="client-info">
            <h3 class="client-name">{{ client.name }}</h3>
            <router-link :to="{ name: 'Client', params: { id: client.id } }" class="details-link">Details</router-link>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'Clients',
  data() {
    return {
      clients: []
    }
  },
  mounted() {
    this.getClients()
  },
  methods: {
    getClients() {
      axios
        .get('/api/v1/clients/')
        .then(response => {
          for (let i = 0; i < response.data.length; i++) {
            this.clients.push(response.data[i])
          }
        })
        .catch(error => {
          console.log(JSON.stringify(error))
        })
    }
  }
}
</script>

<style lang="scss" scoped>
@import "@/assets/styles/client-card.scss";

.page-clients {
  .container {
    .columns {
      .column {
        .title {
          padding: 10px 0;
        }
        .button {
          background-color: #4CAF50;
          color: #fff;
        }
      }
    }
  }
}
</style>