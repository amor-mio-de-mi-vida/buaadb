<template>
	<div>
		<div>
			<homeHeader></homeHeader>
		</div>
		<div class="content1">
			<userSideMenu></userSideMenu>
			<div class="project_card">
				<el-row :gutter="25" style="margin-right: 15px;margin-left: -5px" type="flex" v-loading="loading">
				<el-col v-for="(item, index) in projects" :key="index" class="text item" :span="8">
					<el-card class="box-card">
						<div slot="header" class="clearfix">
							<span>{{item.name}}</span>
						</div>
						<div class="item">
							时间：{{item.time}}
						</div>
						<div class="item">
							地点：{{item.position}}
						</div>
						<el-divider></el-divider>
						<div>
							<el-button @click="viewProject(item.id)" type="text">
								查看详情
							</el-button>
							<el-button @click="quitProject(item.id)" type="text">
								退出项目
							</el-button>
							<!--el-button @click="uploadData(item.id)">
								上传资料
							</el-button-->
							<!--el-button type="text">查看讨论</el-button-->
							<el-button @click="upLoadFile(item)" type="text">上传资料</el-button>
							<div class="submit" v-show="item.dialogVisible">
								<div class="loaderCss">
									<upLoader :project_id="item.id" :lastSubmit="last"></upLoader>
								</div>
							</div>
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
	import upLoader from "@/components/upLoader"
	export default {
		components: {homeHeader, userSideMenu, upLoader},
		data() {
			return {
				last: '',
				dialogVisible: false,
				projects: [
					{
						"id": '1',
						"name": '项目名称',
						"time": '周五 12:00-14:00',
						"position": '操场',
						"description": '这是一项很好的志愿项目',
						"status": '已完成',
						dialogVisible: false,
					},
					{
						"id": '2',
						"name": '项目名称',
						"time": '周五 12:00-14:00',
						"position": '操场',
						"description": '这是一项很好的志愿项目',
						"status": '已完成',
						dialogVisible: false
					},
					{
						"id": '3',
						"name": '项目名称',
						"time": '周五 12:00-14:00',
						"position": '操场',
						"description": '这是一项很好的志愿项目',
						"status": '已完成',
						dialogVisible: false
					},
					{
						"id": '4',
						"name": '项目名称',
						"time": '周五 12:00-14:00',
						"position": '操场',
						"description": '这是一项很好的志愿项目',
						"status": '已完成',
						dialogVisible: false
					},
					{
						"id": '4',
						"name": '项目名称',
						"time": '周五 12:00-14:00',
						"position": '操场',
						"description": '这是一项很好的志愿项目',
						"status": '已完成',
						dialogVisible: false
					},
				]
			}
		},
		async created() {
			await this.axios({
				method: 'post',
				url: 'http://localhost:8000/buaa_db/stu_get_project/',
				headers: {'Content-Type': 'multipart/form-data'},
			}).then((res)=>{
				this.projects = res.data.projects;
			})
		},
		methods: {
			viewProject(id) {
				this.$router.push({
					path: '/project/' + id
				})
			},
			quitProject(id) {
				this.axios({
					method: 'post',
					url: 'http://localhost:8000/buaa_db/stu_apply_project_out/',
					headers: {'Content-Type': 'multipart/form-data'},
					data: {
						'project_id': id
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
			upLoadFile(item) {
				item.dialogVisible = !item.dialogVisible
				this.axios({
					method: 'post',
					url: 'http://localhost:8000/buaa_db/stu_get_feedback/',
					headers: {'Content-Type': 'multipart/form-data'},
					param: {
						'project_id': item.id
					}
				}).then((res)=>{
					this.last = res.data.feedback
				})
			}
		}
	}
</script>

<style scoped>
	.content1 {
		margin-left: 120px;
	}
	.project_card {
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