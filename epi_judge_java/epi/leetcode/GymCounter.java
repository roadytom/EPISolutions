package epi.leetcode;

import java.time.DayOfWeek;
import java.time.LocalDate;
import java.time.temporal.TemporalAdjusters;
import java.util.HashSet;
import java.util.List;
import java.util.Set;
import java.util.TreeMap;

public class GymCounter {
    int count(List<LocalDate> visits) {
        Set<LocalDate> saturdays = new HashSet<>(), sundays = new HashSet<>();
        for (LocalDate d : visits) {
            if (d.getDayOfWeek() == DayOfWeek.SATURDAY) saturdays.add(d);
            else if (d.getDayOfWeek() == DayOfWeek.SUNDAY) sundays.add(d);
        }
        int ans = 0;
        for (var saturday : saturdays) {
            if (sundays.contains(saturday.plusDays(1))) {
                ans++;
            }
        }
        return ans;
    }

    int count2(List<Integer> days) {
        Set<Integer> saturdays = new HashSet<>();
        Set<Integer> sundays = new HashSet<>();
        for (int day : days) {
            // saturday
            if (day % 7 == 5) {
                saturdays.add(day);
            } else if (day % 7 == 6) {
                sundays.add(day);
            }
        }
        int ans = 0;
        for (int saturday : saturdays) {
            if (sundays.contains(saturday + 1)) {
                ans++;
            }
        }
        return ans;
    }
}
