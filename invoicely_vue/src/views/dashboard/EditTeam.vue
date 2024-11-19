<template>
  <div class="page-edit-team">
    <div class="container">
      <nav class="breadcrumb">
        <ul class="breadcrumb-list">
          <li><router-link to="/dashboard" class="breadcrumb-link">Dashboard</router-link></li>
          <li><router-link to="/dashboard/my-account" class="breadcrumb-link">My account</router-link></li>
          <li class="breadcrumb-link is-active"><router-link to="/dashboard/my-account/edit-team">Edit</router-link></li>
        </ul>
      </nav>
      <div class="columns">
        <div class="column">
          <h1 class="title">Edit team</h1>
        </div>
        <div class="column">
          <div class="field">
            <label class="field-label">Name</label>
            <input type="text" class="field-input" v-model="team.name">
          </div>
          <div class="field">
            <label class="field-label">Org. number</label>
            <input type="text" class="field-input" v-model="team.org_number">
          </div>
          <div class="field">
            <label class="field-label">First invoice number</label>
            <input type="number" class="field-input" v-model="team.first_invoice_number">
          </div>
          <div class="field">
            <label class="field-label">Bankaccount</label>
            <input type="text" class="field-input" v-model="team.bankaccount">
          </div>
          <div class="field">
            <label class="field-label">Email</label>
            <input type="email" class="field-input" v-model="team.email">
          </div>
          <div class="field">
            <label class="field-label">Address 1</label>
            <input type="text" class="field-input" v-model="team.address1">
          </div>
          <div class="field">
            <label class="field-label">Address 2</label>
            <input type="text" class="field-input" v-model="team.address2">
          </div>
          <div class="field">
            <label class="field-label">Zipcode</label>
            <input type="text" class="field-input" v-model="team.zipcode">
          </div>
          <div class="field">
            <label class="field-label">Place</label>
            <input type="text" class="field-input" v-model="team.place">
          </div>
          <div class="buttons">
            <button class="button" @click="submitForm">Save</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'EditTeam',
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
    submitForm() {
      axios
        .patch(`/api/v1/teams/${this.team.id}/`, this.team)
        .then(response => {
          this.$router.push('/dashboard/my-account')
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
.page-edit-team {
  .buttons {
    padding: 20px 0;
    .button {
      background-color: #4CAF50;
      font-weight: 600;
      color: #fff;
    }
  }
}
</style>