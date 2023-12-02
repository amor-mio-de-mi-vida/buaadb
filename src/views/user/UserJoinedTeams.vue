<template>
	<div>
		<div>
			<homeHeader></homeHeader>
		</div>
		<div class="content1">
			<userSideMenu></userSideMenu>
			<div class="Team_card">
			<el-empty description="描述文字"></el-empty>
				<el-row :gutter="25" style="margin-right: 15px;margin-left: -5px" type="flex" v-loading="loading">
				<el-col v-for="(item, index) in teams" :key="index" class="text item" :span="8">
					<el-card class="box-card">
						<div slot="header" class="clearfix">
							<span>{{item.name}}</span>
						</div>
						<div class="item">
							团队描述: {{item.profile}}
						</div>
						<el-divider></el-divider>
						<div>
							<el-button @click="viewTeam(item.id)" type="text">
								查看详情
							</el-button>
							<el-button @click="quitTeam(item.id)" type="text">
								退出团队
							</el-button>
						</div>
					</el-card>
				</el-col>
				</el-row>
			</div>
		</div>
	</div>
</template>

<script>
	import homeHeader from "@/components/homeHeader"
	import userSideMenu from "@/components/userSideMenu"
	export default {
		components: {homeHeader, userSideMenu},
		data() {
			return {
				nowId: '',
				last: '',
				dialogVisible: false,
				teams: [
					{
						"id": '1',
						"name": 'xxx团队',
						"profile": 'xxx团体是一个...',
						dialogVisible: false,
					},
				]
			}
		},
		async created() {
			await this.axios({
				method: 'post',
				url: 'http://localhost:8000/buaa_db/stu_get_team/',
				headers: {'Content-Type': 'multipart/form-data'},
			}).then((res)=>{
				console.log(res)
				this.teams = res.data.teams;
			})
		},
		methods: {
			viewTeam(id) {
				this.$router.push({
					path: '/team/' + id
				})
			},
			quitTeam(id) {
				this.axios({
					method: 'post',
					url: 'http://localhost:8000/buaa_db/apply_team_out/',
					headers: {'Content-Type': 'multipart/form-data'},
					data: {
						'team_id': id
					}
				}).then((res)=>{
					if (res.data.status == 200) {
						let msg = this.$message({
							type: 'success',
							message: "退出项目成功"
						});
						setTimeout(()=> {
							msg.close();
						},1000);
					}
					else {
						this.$message({
							type: 'error',
							message: "未加入过该项目"
						});
					}
				})
			},
		}
	}
</script>

<style scoped>
	.content1 {
		margin-left: 120px;
	}
	.Team_card {
		margin-left: 20px;
	}
	.el-divider {
		margin: 10px 0;
	}
	.item {
		padding: 5px;
	}
	.el-row {
		display:flex;
		flex-wrap: wrap;
		align-items: center;
	}
	.el-row  .el-card {
		width: 100%;
		height: 100%;
		margin-right: 20px;
		margin-top: 20px;
		transition: all .5s;
	}
	.el-form-item {
		margin-bottom: 0 !important;
	}
	.pagination-container {
		margin-top: -3px;
		margin-bottom: 30px;
	}
</style>