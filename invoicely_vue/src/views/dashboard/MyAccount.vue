<template>
  <div class="page-my-account">
    <div class="container">
      <nav class="breadcrumb">
        <ul class="breadcrumb-list">
          <li><router-link to="/dashboard" class="breadcrumb-link">Dashboard</router-link></li>
          <li class="breadcrumb-link is-active"><router-link to="/dashboard/my-account">My account</router-link></li>
        </ul>
      </nav>
      <h1 class="title">My account</h1>
      <strong>Team: </strong>{{ team.name }}<br>
      <strong>Username: </strong>{{ $store.state.user.username }}
      <hr>
      <div class="buttons">
        <router-link to="/dashboard/my-account/edit-team" class="button">Edit team</router-link>
        <button @click="logout()" class="button">Log out</button>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'MyAccount',
  data() {
    return {
      team: {}
    }
  },
  async mounted() {
    await this.getOrCreateTeam()
  },
  methods: {
    getOrCreateTeam() {
      axios
        .get("/api/v1/teams/")
        .then(response => {
          this.team = response.data[0]
        })
        .catch(error => {
          console.log(JSON.stringify(error))
        })
    },
    logout() {
      axios
        .post("/api/v1/token/logout/")
        .then(response => {
          axios.defaults.headers.common["Authorization"] = ""
          localStorage.removeItem("username")
          localStorage.removeItem("userid")
          localStorage.removeItem("token")
          this.$store.commit('removeToken')
          this.$router.push('/')
        })
        .catch(error => {
          if (error.response) {
            console.log(JSON.stringify(error.response.data))
          } else if (error.message) {
            console.log(JSON.stringify(error.message))
          } else {
            console.log(JSON.stringify(error))
          }
        })
    }
  }
}
</script>

<style lang="scss" scoped>
.page-my-account {
  .title {
    padding: 10px 0;
  }
  .buttons {
    padding: 10px 0;
    display: flex;
    gap: 10px;
    .button {
      &:nth-child(1) {
        background-color: #e7e7e7; 
        color: black;
      }
      &:nth-child(2) {
        background-color: #f44336;
        color: #fff;
      }
    }
  }
}
</style>