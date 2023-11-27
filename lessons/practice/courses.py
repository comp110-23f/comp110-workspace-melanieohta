"""Function writing practice."""

__author__ = "730671130"

class Course:
    """Models the idea of a UNC course."""
    name: str
    level: int
    prerequisites: list[str]

    def is_valid_course(self, prereq: str) -> bool:
        """Returns True if a course is valid, False if not."""
        if self.level >= 400 and prereq in self.prerequisites:
            return True
        return False

def find_courses(courses: list[Course], prereq: str) -> list[str]:
    """Returns a list of courses whose level is 400+ and whose prereq list contains the given prereq."""
    results: list[str] = []
    for c in courses:
        if c.level >=400:
            for p in c.prerequisites:
                if p == prereq:
                    results.append(c.name)
    return results