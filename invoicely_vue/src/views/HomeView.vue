<template>
  <div class="page-home">
    <div class="container">
      <h1 class="title">Welcome to Invoicely!</h1>
      <template v-if="!$store.state.isAuthenticated">
        <div class="login-info-section">
          <p class="login-info-links">
            <router-link to="/log-in" class="login-info-link">Log in</router-link> to a test profile or 
            <router-link to="/sign-up" class="login-info-link">register</router-link> a new one
          </p>
          <ul class="login-info">
            <li>Login: <span class="login">userOne@gmail.com</span></li>
            <li>Password: <span class="password">1X9T7WWA51</span></li>
          </ul>
        </div>
      </template>
    </div>
  </div>
</template>

<script>
export default {
  name: 'HomeView',
  components: {
  }
}
</script>

<style lang="scss" scoped>
.page-home {
  .title {
    padding: 50px 0;
    text-align: center;
  }
  .login-info-section {
    .login-info-links {
      font-size: 16px;
      text-align: center;
      margin-bottom: 10px;
      .login-info-link {
        color: blue;
        text-decoration: underline;
      }
    }
    .login-info {
      display: flex;
      gap: 20px;
      justify-content: center;
      font-size: 14px;
      text-align: center;
      @media(max-width: 400px) {
        display: block;
        & li:first-child {
          margin-bottom: 10px;
        }
      }
      .login,
      .password {
        font-weight: bold;
      }
    }
  }
}
</style>
