<template>
  <div class="columns">
    <div class="column">
      <div class="field">
        <label class="field-label">Title</label>
        <input type="text" class="field-input" v-model="item.title">
      </div>
      <div class="field">
        <label class="field-label">Price</label>
        <input type="text" class="field-input" v-model="item.unit_price">
      </div>
      <div class="field">
        <label class="field-label">Quantity</label>
        <input type="number" class="field-input" v-model="item.quantity">
      </div>
      <div class="field">
        <label class="field-label">Vat rate</label>
        <div class="select">
          <select class="field-input">
            <option value="0">0%</option>
            <option value="14">14%</option>
            <option value="25">25%</option>
          </select>
        </div>
      </div>
      <div class="field">
        <label class="field-label">Gross amount</label>
        <input type="text" class="field-input" v-bind:value="gross_amount" disabled>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ItemForm',
  props: {
    initialItem: Object
  },
  data() {
    return {
      item: this.initialItem
    }
  },
  computed: {
    gross_amount() {
      const unit_price = this.item.unit_price
      const quantity = this.item.quantity
      const vat_rate = this.item.vat_rate
      this.item.net_amount = unit_price * quantity
      this.$emit('updatePrice', this.item)
      return this.item.net_amount + (this.item.net_amount * (vat_rate / 100))
    }
  }
}
</script>

<style lang="scss" scoped>
@import "@/assets/styles/fomrs.scss";

</style>