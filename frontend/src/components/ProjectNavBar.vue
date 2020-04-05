<template lang="html">
  <span>
  <b-navbar type="dark" variant="dark" class="project-nav">
    <b-navbar-brand href="#">
      Sprinter
    </b-navbar-brand>
    <b-navbar-brand class="text-muted">
      {{name}}
    </b-navbar-brand>
    <b-navbar-nav>
      <b-nav-item>
        Dashboard
      </b-nav-item>
    </b-navbar-nav>
    <b-navbar-nav class="ml-auto">
      <b-nav-item href="#" v-on:click="toggleTeamMenu"><i class="fas fa-users fa-lg"></i></b-nav-item>
    </b-navbar-nav>
  </b-navbar>
  </span>
</template>

<script>
export default {
  props: [
    'name'
  ],
  methods: {
    toggleTeamMenu(){
      document.getElementById('team-menu').classList.toggle('collapsed')
      document.getElementById('tasks-window').classList.toggle('show-team')
    }
  }
}
</script>

<style lang="sass" scoped>
  .project-nav
    z-index: 1
</style>
