<template>
  <div class="page-invoice">
    <div class="container">
      <nav class="breadcrumb">
        <ul class="breadcrumb-list">
          <li><router-link to="/dashboard" class="breadcrumb-link">Dashboard</router-link></li>
          <li><router-link to="/dashboard/invoices" class="breadcrumb-link">Invoices</router-link></li>
          <li class="breadcrumb-link is-active"><router-link :to="{ name: 'Invoice', params: { id: invoice.id } }">{{ invoice.invoice_number }}</router-link></li>
        </ul>
      </nav>
      <div class="columns">
        <div class="column">
          <h1 class="title">Invoice - {{ invoice.invoice_number }}</h1>
          <div class="buttons">
            <button @click="getPdf()" class="button">Download PDF</button>
            <template v-if="!invoice.is_credit_for && !invoice.is_credited">
              <button @click="setAsPaid()" class="button" v-if="!invoice.is_paid">Set as paid</button>
              <button @click="createCreditNote()" class="button" v-if="!invoice.is_paid">Create credit note</button>
            </template>
            <button @click="sendReminder()" class="button" v-if="!invoice.is_paid && !invoice.is_credit_for">Send reminder</button>
          </div>
        </div>
        <div class="column">
          <h3 class="title">Client</h3>
          <p><strong>{{ invoice.client_name }}</strong></p>
          <p v-if="invoice.client_address1">{{ invoice.client_address1 }}</p>
          <p v-if="invoice.client_address1">{{ invoice.client_address2 }}</p>
          <p v-if="invoice.client_address1 || invoice.client_place">{{ invoice.client_zipcode }} {{ invoice.client_place }}</p>
          <p v-if="invoice.client_country">{{ invoice.client_country }}</p>
        </div>
        <div class="column">
          <h3 class="title">Items</h3>
          <div class="table-section">
            <table class="table">
              <thead>
                <tr>
                  <th>Title</th>
                  <th>Quantity</th>
                  <th>Vat rate</th>
                  <th>Total</th>
                </tr>
              </thead>
              <tbody>
                <tr
                  v-for="item in invoice.items"
                  v-bind:key="item.id"
                >
                  <td>{{ item.title }}</td>
                  <td>{{ item.quantity }}</td>
                  <td>{{ item.vat_rate }}%</td>
                  <td>{{ getItemTotal(item) }}</td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
        <div class="column">
          <h3 class="title">Summary</h3>
          <div class="columns">
            <div class="column">
              <p><strong>Net amount</strong>: {{ invoice.net_amount }}</p>
              <p><strong>Vat amount</strong>: {{ invoice.vat_amount }}</p>
              <p><strong>Gross amount</strong>: {{ invoice.gross_amount }}</p>
              <p><strong>Bankaccount</strong>: {{ invoice.bankaccount }}</p>
            </div>
            <div class="column">
              <p><strong>Our reference</strong>: {{ invoice.sender_reference }}</p>
              <p><strong>Client reference</strong>: {{ invoice.client_contact_reference }}</p>
              <p><strong>Due date</strong>: {{ invoice.get_due_date_formatted }}</p>
              <p><strong>Status</strong>: {{ getStatusLabel() }}</p>
              <p><strong>Invoice type</strong>: {{ getInvoiceType() }}</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
const fileDownload = require('js-file-download')
export default {
  name: 'Invoice',
  data() {
    return {
      invoice: {},
      items: []
    }
  },
  mounted() {
    this.getInvoice()
  },
  methods: {
    getInvoice() {
      const invoiceID = this.$route.params.id

      axios
        .get(`/api/v1/invoices/${invoiceID}`)
        .then(response => {
          this.invoice = response.data
        })
        .catch(error => {
          console.log(JSON.stringify(error))
        })
    },
    getPdf() {
      const invoiceID = this.$route.params.id
      axios
        .get(`/api/v1/invoices/${invoiceID}/generate_pdf/`, {
          responseType: 'blob',
        }).then(res => {
          fileDownload(res.data, `invoice_${invoiceID}.pdf`);
        }).catch(err => {
          console.log(err);
        })
    },
    getStatusLabel() {
      if (this.invoice.is_paid) {
        return 'Is paid'
      } else {
        return 'Is not paid'
      }
    },
    getInvoiceType() {
      if (this.invoice.invoice_type === 'credit_note') {
        return 'Credit note'
      } else {
        return 'invoice'
      }
    },
    getItemTotal(item) {
      const unit_price = item.unit_price
      const quantity = item.quantity
      const total = item.net_amount + (item.net_amount * (item.vat_rate/100))
      return parseFloat(total).toFixed(2)
    },
    async setAsPaid() {
      this.invoice.is_paid = true
      let items = this.invoice.items
      delete this.invoice['items']
      await axios
        .patch(`/api/v1/invoices/${this.invoice.id}/`, this.invoice)
        .then(response => {

        })
        .catch(error => {
          console.log(JSON.stringify(error))
        })
      this.invoice.items = items
    },
    async createCreditNote() {
      this.invoice.is_credited = true
      let items = this.invoice.items
      delete this.invoice['items']
      await axios
        .patch(`/api/v1/invoices/${this.invoice.id}/`, this.invoice)
        .then(response => {

        })
        .catch(error => {
          console.log(JSON.stringify(error))
        })
      this.invoice.items = items
      let creditNote = this.invoice
      creditNote.is_credit_for = this.invoice.id
      creditNote.is_credited = false
      creditNote.invoice_type = 'credit_note'
      delete creditNote['id']
      await axios
        .post('api/v1/invoices/', creditNote)
        .then(response => {
          this.$router.push('/dashboard/invoices')
        })
        .catch(error => {
          console.log(JSON.stringify(error))
        })
    },
    sendReminder() {
      axios
        .get(`/api/v1/invoices/${this.invoice.id}/send_reminder/`)
        .then(responce => {
          console.log('Reminder sent successfully:', response.data);
        })
        .catch(error => {
          console.log(JSON.stringify(error))
        })
    }
  }
}
</script>

<style lang="scss" scoped>
@import "@/assets/styles/table.scss";

.page-invoice {
  .container {
    .columns {
      .column {
        .title {
          padding: 10px 0;
        }
        .buttons {
          display: flex;
          align-items: center;
          flex-wrap: wrap;
          gap: 10px;
          .button {
            width: 160px;
            font-size: 16px;
            padding: 5px 12px;
            @media(max-width: 400px) {
              width: 100%;
            }
          }
        }
        .table-section {
          .table {
            @media(max-width: 768px) {
              width: 760px;
            }
          }
        }
      }
    }
  }
}
</style>