<template>
  <div class="page-dashboard">
    <div class="container">
      <div class="colums">
        <div class="column">
          <h1 class="title">Dashboard</h1>
        </div>
        <div class="column">
          <h2 class="table-title">Unpaid invoices</h2>
          <div class="table-section">
            <table class="table">
              <thead>
                <tr>
                  <th>#</th>
                  <th>Client</th>
                  <th>Amount</th>
                  <th>Due date</th>
                  <th></th>
                </tr>
              </thead>
              <tbody>
                <tr
                  v-for="invoice in invoices"
                  v-bind:key="invoice.id"
                >
                  <td>{{ invoice.invoice_number }}</td>
                  <td>{{ invoice.client_name }}</td>
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
      <div class="colums">
        <div class="column">
          <h2 class="client-list-title">Newest clients</h2>
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
          <!-- <div
            v-for="client in clients"
            v-bind:key="client.id"
          >
            <div class="box">
              <h3 class="box-title">{{ client.name }}</h3>
              <router-link :to="{ name: 'Client', params: { id: client.id } }" class="button">Details</router-link>
            </div>
          </div> -->
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'Dashboard',
  data() {
    return {
      invoices: [],
      clients: []
    }
  },
  mounted() {
    this.getInvoices()
    this.getClients()
  },
  methods: {
    getInvoices() {
      axios
        .get('/api/v1/invoices/')
        .then(response => {
          for (let i = 0; i < response.data.length; i++) {
            if (!response.data[i].is_credit_for) {
              this.invoices.push(response.data[i])
            }
          }
        })
        .catch(error => {
          console.log(JSON.stringify(error))
        })
    },
    getClients() {
      axios
        .get('/api/v1/clients/')
        .then(response => {
          for (let i = 0; i < response.data.length; i++) {
            if (this.clients.length < 5) {
              this.clients.push(response.data[i])
            }
          }
        })
        .catch(error => {
          console.log(JSON.stringify(error))
        })
    }
  },
  computed: {
    unpaidInvoices() {
      return this.invoices.filter(invoice => invoice.is_paid == false)
    }
  }
}
</script>


<style lang="scss" scoped>
@import "@/assets/styles/table.scss";
@import "@/assets/styles/client-card.scss";

.page-dashboard {
  .container {
    .colums {
      .column {
        .title {
          padding: 10px 0 20px 0;
        }
        .table-title {
          padding-bottom: 10px;
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
        .client-list-title {
          padding: 20px 0 10px 0;
        }
        .clients-list {
          padding: 0 0 20px 0;
        }
      }
    }
  }
}
</style>