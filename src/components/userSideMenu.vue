<template>
    <el-col :span="6" class="side_menu">
        <el-menu default-active="$router.path" class="el-menu-vertical-demo">
            <el-menu-item index="/user_page/" @click="click1()">
                <i class="el-icon-menu"></i>
                <span slot="title">个人信息</span>
            </el-menu-item>
            <el-menu-item index="joined_project" @click="click2()">
                <i class="el-icon-document"></i>
                <span slot="title">已加入项目</span>
            </el-menu-item>
            <el-menu-item index="joined_team" @click="click3()">
                <i class="el-icon-setting"></i>
                <span slot="title">已加入圈子</span>
            </el-menu-item>
        </el-menu>
    </el-col>
</template>

<script>
    export default {
        data() {
            return {

            }
        },
        methods: {
            click1() {
                this.$router.push({
                    path: '/user_page/'
                });
            },
            click2() {
                this.$router.push({
                    path: '/joined_project/'
                });
            },
            click3() {
                this.$router.push({
                    path: '/joined_team/'
                });
            }
        }
    }
</script>

<style scoped>
    .side_menu {
        width: 200px;
        height: 100%;
        margin-right: 0px;
    }
</style>