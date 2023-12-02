<template>
	<div class="header">
		<router-link :to="'/CheckCreateProjectApply/'" style="text-decoration: none;">
			<h1>Home</h1>
		</router-link>
		<el-menu :default-active="activeIndex" class="el-menu-demo" mode="horizontal" @select="handleSelect">
		<!--一级导航栏-->
		<el-menu-item index="1">
			<router-link :to="'/CheckCreateProjectApply/'" style="text-decoration: none;">待审核项目</router-link>
		</el-menu-item>
		<el-menu-item index="2">
			<router-link :to="'/CheckCreateTeamApply/'" style="text-decoration: none;">待审核团体</router-link>
		</el-menu-item>
		<el-menu-item>
			<el-button type="text" @click="logOut()">退出登录</el-button>
		</el-menu-item>
		</el-menu>
	</div>
	</template>

	<script>
	export default {
		name: "sysManagerHomeHeader",
		date() {
			return {

			};
		},
		methods: {
			logOut() {
				this.axios({
					method: 'post',
					url: 'http://localhost:8000/buaa_db/logout/',
					headers: {'Content-Type': 'multipart/form-data'},
					data: ''
				}).then((res)=>{
					if (res.data.status == 200) {
						let msg = this.$message({
							type: 'success',
							message: "退出登录成功"
						});
						setTimeout(()=> {
							msg.close();
						},1000);
						this.$router.push({path: '/login/'})
					}
					else if (res.data.status == 400) {
						this.$message({
							type: 'error',
							message: '退出登录失败'
						})
					}
				})
			}
		}
	}
	</script>

	<!--scoped修改默认值-->
	<style scoped>
	.header {
		margin-left: 100px;
		margin-right: 100px;
	}

	.item {
		padding: 0 0;
	}

	div /deep/ .submenu{
		margin-bottom: 20px;
	}
	</style>