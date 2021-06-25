from _repobee import plugin
import repobee_plug as plug

from repobee_reviewothers import reviewothers


teams = [
        plug.StudentTeam(members=members)
        for members in (["a"], ["b", "c"], ["d", "e"])
    ]

graders = plug.StudentTeam(members=["d", "e"])

def test_register():
    """Just test that there is no crash"""
    plugin.register_plugins([reviewothers])

class TestReviewOthers:

    def test_all_students_get_reviewed(self):
        """All students should get a review team."""

        allocations = reviewothers.make_actual_allocations(teams, graders)
        assert sorted(teams) == sorted(
            [alloc.reviewed_team for alloc in allocations]
        )

    def test_all_students_get_same_graders(self):
        """All students should get a review team."""

        allocations = reviewothers.make_actual_allocations(teams, graders)

        for grader_team, student_team in allocations:
            assert set(grader_team.members) == set(graders.members)
