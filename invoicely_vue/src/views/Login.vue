<template>
  <div class="page-login">
    <div class="container">
      <div class="form-setion">
        <form @submit.prevent="submitForm" class="login-form">
          <h1 class="title">Log in</h1>
          <div class="field">
            <label class="field-label">E-mail</label>
            <div class="field-icon field-email">
              <input type="email" name="username" class="field-input" v-model="username">
            </div>
          </div>
          <div class="field">
            <label class="field-label">Password</label>
            <div class="field-icon field-password">
              <input type="password" name="password" class="field-input" v-model="password">
            </div>
          </div>
          <div class="notification" v-if="errors.length">
            <p v-for="error in errors" v-bind:key="error" class="notification-text">
              {{ error }}
            </p>
          </div>
          <div class="buttons">
            <button class="button">Log in</button>
          </div>
          <div class="links">
            <router-link to="/sign-up" class="link">Click here</router-link> to sign up!
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'Login',
  data() {
    return {
      username: '',
      password: '',
      errors: []
    }
  },
  methods: {
    async submitForm(e) {
      axios.defaults.headers.common["Authorization"] = ""
      localStorage.removeItem("token")
      const formData = {
        username: this.username,
        password: this.password
      }

      await axios
        .post("/api/v1/token/login/", formData)
        .then(response => {
          const token = response.data.auth_token
          this.$store.commit('setToken', token)
          axios.defaults.headers.common["Authorization"] = "Token " + token
          localStorage.setItem("token", token)
        })
        .catch(error => {
          if (error.response) {
            const errors = error.response.data;
            if (errors.non_field_errors) {
              this.errors.push(errors.non_field_errors.join(", "));
            } else {
              for (const property in errors) {
                if (property !== "non_field_errors") {
                  this.errors.push(`${property}: ${errors[property]}`);
                }
              }
            }
            console.log(JSON.stringify(error.response.data))
          } else if (error.message) {
            console.log(JSON.stringify(error.message))
          } else {
            console.log(JSON.stringify(error))
          }
        })
      axios
        .get("/api/v1/users/me")
        .then(response => {
          this.$store.commit('setUser', {'username': response.data.username, 'id': response.data.id})
          localStorage.setItem('username', response.data.username)
          localStorage.setItem('userid', response.data.id)
          this.$router.push('/dashboard')
        })
        .catch(error => {
          console.log(JSON.stringify(error))
        })
    }
  }
}
</script>

<style lang="scss" scoped>
@import "@/assets/styles/authentication-form.scss";
</style>