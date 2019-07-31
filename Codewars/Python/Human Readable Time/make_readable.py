import unittest


def make_readable(seconds):
    h = seconds // (60 * 60)
    m = (seconds - h * 60 * 60) // 60
    s = seconds - (h * 60 * 60) - (m * 60)
    if h < 10:
        h = "0" + str(h)

    if m < 10:
        m = "0" + str(m)

    if s < 10:
        s = "0" + str(s)

    return str(h) + ":" + str(m) + ":" + str(s)


class HumanReadableTime(unittest.TestCase):
    def test(self):
        self.assertEqual(make_readable(0), "00:00:00")
        self.assertEqual(make_readable(5), "00:00:05")
        self.assertEqual(make_readable(60), "00:01:00")
        self.assertEqual(make_readable(86399), "23:59:59")
        self.assertEqual(make_readable(359999), "99:59:59")


if __name__ == "__main__":
    unittest.main()
