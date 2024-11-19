<template>
  <div class="page-invoices">
    <div class="container">
      <nav class="breadcrumb">
        <ul class="breadcrumb-list">
          <li><router-link to="/dashboard" class="breadcrumb-link">Dashboard</router-link></li>
          <li class="breadcrumb-link is-active"><router-link to="/dashboard/invoices">Invoices</router-link></li>
        </ul>
      </nav>
      <div class="columns">
        <div class="column">
          <h1 class="title">Invoices</h1>
        </div>
        <div class="column">
          <div class="table-section">
            <table class="table">
              <thead>
                <tr>
                  <th>#</th>
                  <th>Client</th>
                  <th>Amount</th>
                  <th>Due date</th>
                  <th>Is paid</th>
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
                  <td>{{ getStatusLabel(invoice) }}</td>
                  <td><router-link :to="{ name: 'Invoice', params: { id: invoice.id } }" class="details-link">Details</router-link></td>
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
  name: 'Invoices',
  data() {
    return {
      invoices: []
    }
  },
  mounted() {
    this.getInvoices()
  },
  methods: {
    getInvoices() {
      axios
        .get('/api/v1/invoices/')
        .then(response => {
          for (let i = 0; i < response.data.length; i++) {
            this.invoices.push(response.data[i])
          }
        })
        .catch(error => {
          console,log(JSON.stringify(error))
        })
    },
    getStatusLabel(invoice) {
      if (invoice.is_paid) {
        return 'Yes'
      } else {
        return 'No'
      }
    }
  }
}
</script>

<style lang="scss" scoped>
@import "@/assets/styles/table.scss";

.page-invoices {
  .container {
    .columns {
      .column {
        .title {
          padding: 10px 0;
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