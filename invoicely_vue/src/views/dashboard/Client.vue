<template>
  <div class="page-clients">
    <div class="container">
      <nav class="breadcrumb">
        <ul class="breadcrumb-list">
          <li><router-link to="/dashboard" class="breadcrumb-link">Dashboard</router-link></li>
          <li><router-link to="/dashboard/clients" class="breadcrumb-link">Clients</router-link></li>
          <li class="breadcrumb-link is-active"><router-link :to="{ name: 'Client', params: { id: client.id } }">{{ client.name }}</router-link></li>
        </ul>
      </nav>
      <div class="columns">
        <div class="column">
          <h1 class="title">{{ client.name }}</h1>
          <router-link :to="{ name: 'EditClient', params: { id: client.id } }" class="button">Edit</router-link>
        </div>
        <div class="column">
          <h2 class="title">Contact details</h2>
          <p><strong>{{ client.name }}</strong></p>
          <p v-if="client.address1">{{ client.address1 }}</p>
          <p v-if="client.address1">{{ client.address2 }}</p>
          <p v-if="client.address1 || client.place">{{ client.zipcode }} {{ client.place }}</p>
          <p v-if="client.country">{{ client.country }}</p>
        </div>
        <div class="column" v-if="unpaidInvoices.length">
          <h2 class="title">Unpaid invoices</h2>
          <div class="table-section">
            <table class="table">
              <thead>
                <tr>
                  <th>#</th>
                  <th>Amount</th>
                  <th>Due date</th>
                  <th></th>
                </tr>
              </thead>
              <tbody>
                <tr
                  v-for="invoice in unpaidInvoices"
                  v-bind:key="invoice.id"
                >
                  <td>{{ invoice.invoice_number }}</td>
                  <td>{{ invoice.gross_amount }}</td>
                  <td>{{ invoice.get_due_date_formatted }}</td>
                  <td>
                    <router-link :to="{ name: 'Invoice', params: { id: invoice.id } }" class="details-link">Details</router-link>
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
        <div class="column" v-if="paidInvoices.length">
          <h2 class="title">Paid invoices</h2>
          <div class="table-section">
            <table class="table">
              <thead>
                <tr>
                  <th>#</th>
                  <th>Amount</th>
                  <th>Due date</th>
                  <th></th>
                </tr>
              </thead>
              <tbody>
                <tr
                  v-for="invoice in paidInvoices"
                  v-bind:key="invoice.id"
                >
                  <td>{{ invoice.invoice_number }}</td>
                  <td>{{ invoice.gross_amount }}</td>
                  <td>{{ invoice.get_due_date_formatted }}</td>
                  <td>
                    <router-link :to="{ name: 'Invoice', params: { id: invoice.id } }" class="details-link">Details</router-link>
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'Client',
  data() {
    return {
      client: {
        invoices: []
      }
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
    }
  },
  computed: {
    unpaidInvoices() {
      return this.client.invoices.filter(invoice => invoice.is_paid == false)
    },
    paidInvoices() {
      return this.client.invoices.filter(invoice => invoice.is_paid == true)
    }
  }
}
</script>

<style lang="scss" scoped>
@import "@/assets/styles/table.scss";
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
        .table-section {
          .table {
            @media(max-width: 768px) {
              width: 760px;
            }
            .details-link {
              color: blue;
            }
          }
        }
      }
    }
  }
}
</style>