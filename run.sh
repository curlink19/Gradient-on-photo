for number in {1..19}; do
	if [ -f "./samples/$number.png" ]; then
		echo -n "$number.png" > .input
		python3 main.py
	fi
	if [ -f "./samples/$number.jpg" ]; then
                echo -n "$number.jpg" > .input
                python3 main.py
	fi
        if [ -f "./samples/$number.jpeg" ]; then
                echo -n "$number.jpeg" > .input
                python3 main.py
	fi
	done
