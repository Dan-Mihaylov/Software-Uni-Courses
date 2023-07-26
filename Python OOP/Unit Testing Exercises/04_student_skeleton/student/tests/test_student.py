from project.student import Student
import unittest


class StudentTester(unittest.TestCase):

    def setUp(self) -> None:

        self.student = Student("Name", {"Math": ["Note 1"]})

    def test__init_with_all_info(self):
        self.assertEqual("Name", self.student.name)
        self.assertEqual({"Math": ["Note 1"]}, self.student.courses)

        self.student = Student("Name")

        self.assertEqual("Name", self.student.name)
        self.assertEqual({}, self.student.courses)

    def test__enroll_same_course__add_notes_return_message(self):

        result_return = self.student.enroll("Math", ["Note 2"])
        expected_course_notes = ["Note 1", "Note 2"]
        result_notes = self.student.courses["Math"]

        expected_return = "Course already added. Notes have been updated."

        self.assertEqual(expected_course_notes, result_notes)
        self.assertEqual(expected_return, result_return)

    def test__enroll_course_with_without_notes__add_course_with_without_notes(self):

        student = Student("Name")

        result_return = student.enroll("Course", ["Note"])
        expected_result = "Course and course notes have been added."

        expected_courses = {"Course": ["Note"]}
        result_courses = student.courses

        self.assertEqual(expected_result, result_return)
        self.assertEqual(expected_courses, result_courses)

        student = Student("Name")

        result_return = student.enroll("Course", ["Note"], "Y")
        expected_result = "Course and course notes have been added."

        expected_courses = {"Course": ["Note"]}
        result_courses = student.courses

        self.assertEqual(expected_result, result_return)
        self.assertEqual(expected_courses, result_courses)

        student = Student("Name")

        result_return = student.enroll("Course", ["Note"], "N")
        expected_result = "Course has been added."

        expected_courses = {"Course": []}
        result_courses = student.courses

        self.assertEqual(expected_result, result_return)
        self.assertEqual(expected_courses, result_courses)

    def test__add_notes_into_existing_course__return_correct_message_add_notes(self):

        result_return = self.student.add_notes("Math", "Note 2")
        expected_result = "Notes have been updated"

        result_notes = self.student.courses["Math"]
        expected_notes = ["Note 1", "Note 2"]

        self.assertEqual(expected_result, result_return)
        self.assertEqual(expected_notes, result_notes)

    def test__add_notes_into_non_existing_course__raise_exception(self):

        with self.assertRaises(Exception) as ex:
            self.student.add_notes("Course", "Notes")

        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test__leave_existing_course__remove_course_return_message(self):

        result_message = self.student.leave_course("Math")
        expected_message = "Course has been removed"

        result_courses = self.student.courses
        expected_courses = {}

        self.assertEqual(expected_message, result_message)
        self.assertEqual(expected_courses, result_courses)

    def test__leave_non_existing_course__raise_exception(self):

        with self.assertRaises(Exception) as ex:
            self.student.leave_course("Course")

        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))


if __name__ == "__main__":
    unittest.main()

