<template>
  <div id="app">
    <b-navbar toggleable="md" type="dark" variant="info">
      <b-container>
        <b-nav-toggle target="nav_collapse"></b-nav-toggle>
        <b-navbar-brand :to="{'name': 'index'}">My Crypto Portfolio</b-navbar-brand>

        <b-collapse is-nav id="nav_collapse">
          <b-nav is-nav-bar>
            <b-nav-item :to="{'name': 'index'}">Dashboard</b-nav-item>
          </b-nav>
        </b-collapse>
      </b-container>
    </b-navbar>
    <router-view></router-view>
  </div>
</template>

<script>

export default {
  name: 'app'
}

</script>

<style>

  .page {
    padding-left: 12px;
    padding-right: 12px;
  }

  .page-header {
  }

  .row {
    padding: 15px 0px;
  }

  .no-margin {
    margin: 0;
  }

</style>
