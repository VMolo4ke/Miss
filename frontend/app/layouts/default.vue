<template>
  <div class="container">
    <slot />
  </div>
</template>

<style lang="scss" scoped>
.container {
  background: $bg-app;
  width: 100%;
  max-width: $max-width;
  margin: 0 auto;
  min-height: 100vh;
}
</style>
