<template>
<div class="wrapper">
  <div id="header-section">
    <div class="container">
      <div class="header">
        <div class="header-logo">
          <img class="header-logo-img" src="./assets/logo_after_img.svg" alt="">
          <router-link to="/" class="logo-link"><strong>Invoicely</strong></router-link>
        </div>
        <nav class="header-menu" :class="{ open: isOpen }">
          <div class="menu-list">
            <template v-if="$store.state.isAuthenticated">
              <router-link to="/dashboard" class="link" @click="toggleBurger">Dashboard</router-link>
              <router-link to="/dashboard/clients" class="link"  @click="toggleBurger">Clients</router-link>
              <router-link to="/dashboard/invoices" class="link"  @click="toggleBurger">Invoices</router-link>
              <div class="buttons">
                <router-link to="/dashboard/invoices/add" class="button" @click="toggleBurger">Add invoice</router-link>
                <router-link to="/dashboard/my-account" class="button" @click="toggleBurger">My account</router-link>
              </div>
            </template>
            <template v-else>
              <router-link to="/" class="link" @click="toggleBurger">Home</router-link>
              <div class="buttons">
                <router-link to="/sign-up" class="button"  @click="toggleBurger"><strong>Sign up</strong></router-link>
                <router-link to="/log-in" class="button"  @click="toggleBurger"><strong>Log in</strong></router-link>
              </div>
            </template>
          </div>
        </nav>
        <div class="burger-icon" :class="{ open: isOpen }" @click="toggleBurger">
          <span></span>
          <span></span>
          <span></span>
          <span></span>
        </div>
      </div>
    </div>
  </div>
  <section class="section">
    <router-view/>
  </section>
</div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'App',
  beforeCreate() {
    this.$store.commit('initializeStore')
    const token = this.$store.state.token
    if (token) {
      axios.defaults.headers.common['Authorization'] = "Token " + token
    } else {
      axios.defaults.headers.common['Authorization'] = ""
    }
  },
  data() {
    return {
      isOpen: false,
    }
  },
  mounted() {
    document.title = "Invoicely";
  },
  methods: {
    toggleBurger() {
      this.isOpen = !this.isOpen;
      if (this.isOpen) {
        document.body.classList.add('no-scroll');
      } else {
        document.body.classList.remove('no-scroll');
      }
    }
  },
}
</script>

<style lang="scss">
#header-section {
  position: fixed;
  width: 100%;
  top: 0;
  left: 0;
  z-index: 50;
  &::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: #07575B;
    z-index: 2;
  }
  .container {
    .header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-size: 20px;
      font-weight: 600;
      height: 80px;
      .header-logo {
        position: relative;
        z-index: 2;
        font-weight: 700;
        display: flex;
        align-items: center;
        gap: 10px;
        @media(max-width: 768px) {
          gap: 5px;
        }
        .header-logo-img {
          height: 40px;
          width: 40px;
          @media(max-width: 768px) {
            height: 30px;
            width: 30px;
          }
        }
        .logo-link {
          position: relative;
          color: #fff;
          font-size: 40px;
          @media(max-width: 768px) {
            font-size: 25px;
            // padding-top: 5px;
          }
        }
      }
      .header-menu {
        position: relative;
        z-index: 2;
        display: flex;
        justify-content: center;
        gap: 20px;     
        transition: left .5s ease;
        @media(max-width: 875px) {
          position: absolute;
          width: 100%;
          top: 80px;
          background-color: rgba(102, 165, 173, 0.95);
          left: -100%;
          height: 100vh;
          padding: 100px 0 0 0;
          
        }
        .menu-list {
          display: flex;
          align-items: center;
          gap: 20px;
          font-size: 18px;
          color: #fff;
          @media(max-width: 875px) {
            font-size: 16px;
            flex-direction: column;
          }
          // .link {

          // }
          .buttons {
            display: flex;
            align-items: center;
            gap: 20px;
            @media(max-width: 875px) {
              flex-direction: column;
            }
            .button {
              background-color: #4CAF50;
              @media(max-width: 875px) {
                font-size: 16px;
              }
            }
          }
        }
        &.open {
          left: 0;
        }
      }
      .burger-icon {
        z-index: 2;
        display: none;
        width: 35px;
        height: 20px;
        position: relative;
        transform: rotate(0deg);
        transition: .5s ease-in-out;
        cursor: pointer;
        @media(max-width: 875px) {
          display: block;
        }
        & span {
          display: block;
          position: absolute;
          height: 3px;
          width: 100%;
          background: #fff;
          border-radius: 5px;
          opacity: 1;
          left: 0;
          transform: rotate(0deg);
          transition: .25s ease-in-out;
          &:nth-child(1) {
            top: 0px;
          }
          &:nth-child(2),
          &:nth-child(3) {
            top: 10px;
          }
          &:nth-child(4) {
            top: 20px;
          }
        }
        &.open span:nth-child(1) {
          top: 18px;
          width: 0%;
          left: 50%;
        }
        &.open span:nth-child(2) {
          transform: rotate(45deg);
        }
        &.open span:nth-child(3) {
          transform: rotate(-45deg);
        }
        &.open span:nth-child(4) {
          top: 18px;
          width: 0%;
          left: 50%;
        }
      }
    }
  }
}
</style>
