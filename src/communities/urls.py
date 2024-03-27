from django.urls import path

from . import views

app_name = "communities"
urlpatterns = [
    path("create_community/", views.create_community, name="create_community"),
    path("save_community", views.save_community, name="save_community"),
    path("admin_community_home/", views.admin_community_home, name="admin_community_home"),
    path("<int:community_id>/dashboard/", views.community_dashboard, name="dashboard"),

    # community joining / leaving
    path("join_a_community/", views.join_a_community, name="join_a_community"),
    path("join_community_error/", views.join_community_error, name="join_community_error"),
    path("join_success/", views.join_success, name="join_success"),
    path("join_community", views.join_community, name="join_community"),

    # urls for report management
    path("<int:community_id>/create_report/", views.create_report, name="create_report"),
    path("<int:community_id>/save_report/", views.save_report, name="save_report"),
    path("<int:community_id>/report/<int:report_id>/", views.view_report, name="view_report"),
    path("<int:community_id>/report/<int:report_id>/edit/", views.edit_report, name="edit_report"),
    path("<int:community_id>/change_admin_status/<int:member_id>/", views.change_admin_status, name="change_admin_status"),
    path("<int:community_id>/remove_member/<int:member_id>/", views.remove_member, name="remove_member"),
    path("<int:community_id>/community_members/", views.community_members, name="community_members"),
]