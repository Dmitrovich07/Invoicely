<template>
  <div class="page-signup">
    <div class="container">
      <div class="form-setion">
        <form @submit.prevent="submitForm" class="signup-form">
          <h1 class="title">Sign up</h1>
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
            <button class="button">Sign up</button>
          </div>
          <div class="links">
            <router-link to="/log-in" class="link">Click here</router-link> to log in!
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'SignUp',
  data() {
    return {
      username: '',
      password: '',
      errors: []
    }
  },
  methods: {
    submitForm(e) {
      const formData = {
        username: this.username,
        password: this.password
      }

      axios
        .post("/api/v1/users/", formData)
        .then(response => {
          console.log(response)
          this.$router.push('/log-in')
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
    }
  }
}
</script>


<style lang="scss" scoped>
@import "@/assets/styles/authentication-form.scss";
</style>