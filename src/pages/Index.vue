<template>

  <b-container class="page">
    <b-row>
      <b-col>
        <h1 class='page-header text-center'>My Portfolio</h1>
      </b-col>
    </b-row>
    <b-row>
      <b-col>
        <b-nav class="float-right">
          <b-button v-b-modal.addTransactionModal size="sm" variant="info"><i class="fa fa-plus"></i> Add transaction</b-button>
        </b-nav>
      </b-col>
    </b-row>
    <b-row>
      <b-col lg>
        <b-card no-body>
          <b-tabs ref="tabs" card>
            <b-tab title="Portfolio" active>
              <b-table hover :items="items"></b-table>
            </b-tab>
            <b-tab title="Charts">
            </b-tab>
          </b-tabs>
        </b-card>
      </b-col>
    </b-row>

    <c-add-transaction-modal></c-add-transaction-modal>
  </b-container>

</template>

<script>
const items = [
  {isActive: true, age: 40, first_name: 'Dickerson', last_name: 'Macdonald'},
  {isActive: false, age: 21, first_name: 'Larsen', last_name: 'Shaw'},
  {isActive: false, age: 89, first_name: 'Geneva', last_name: 'Wilson'},
  {isActive: true, age: 38, first_name: 'Jami', last_name: 'Carney'}
]

import AddTransactionModal from '../components/AddTransactionModal'

export default {

  name: 'index',
  data () {
    return {
      items: items
    }
  },
  components: {
    'c-add-transaction-modal': AddTransactionModal
  }

}

</script>

<style scoped>

</style>
