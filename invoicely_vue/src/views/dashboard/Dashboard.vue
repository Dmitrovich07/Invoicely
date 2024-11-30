<template>
  <div class="page-dashboard">
    <div class="container">
        <h1 class="title">Dashboard</h1>
        <div class="dashboard">
          <div class="unpaid-invoices-block">
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
          <div class="newest-clients-block">
            <h2 class="list-title">Newest clients</h2>
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
    .title {
      padding: 10px 0;
    }
    .dashboard {
      display: flex;
      @media(max-width: 1050px) {
        display: block;
      }
      .unpaid-invoices-block {
        width: 100%;
        .table-title {
          text-align: center;
        }
        .table-section {
          padding: 20px 0;
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
      .newest-clients-block {
        width: 500px;
        @media(max-width: 1050px) {
          width: 100%;
        }
        .list-title {
          text-align: center;
        }
        .clients-list {
          display: flex;
          justify-content: center;
          @media(max-width: 1050px) {
            justify-content: start;
          }
        }
      }
    }
  }
}
</style>

