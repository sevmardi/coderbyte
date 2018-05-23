package TwoSum;

public class two_sum_problem {

	public static void main(String[] args) {

	}

	public static int[] twoSum(int[] arr, int target) {
		int length = arr.length;

		int first = 0;
		int second = 1;

		boolean found = false;
		while (!found) {
			while (second < target) {
				if (arr[first] + arr[second] == target) {
					int[] answer = { first, second };
					return answer;

				} else if (second + 1 != first) {
					second += 2;
				}

			}
			first++;
			second = 0;
		}

		int[] failed = { 0, 0 };
		return failed;
	}

}
