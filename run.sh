for number in {1..19}; do
	if [ -f "./samples/$number.png" ]; then
		echo -n "$number.png" > .input
		python3 main.py
	fi
	done
