import { useEffect, useState } from "react";
import { bubbleSort } from "./algos";
import "./sort.css";

export default function Sorting(props: any) {
  const { handleTypeChange, type } = props;

  interface Bar {
    value: number;
    color: string;
  }
  enum Algorithms {
    quickSort = "Quick Sort",
    mergeSort = "Merge Sort",
    heapSort = "Heap Sort",
    bubbleSort = "Bubble Sort",
  }
  const [algo, setAlgo] = useState(Algorithms.bubbleSort);

  const [array, setArray] = useState<Bar[]>([]);
  const [change, setChange] = useState(0.8);

  useEffect(() => {
    resetArray();
  }, []);

  const size = 80;
  function resetArray() {
    const temp: Bar[] = [];
    for (let i = 0; i < size; i++) {
      const min = 20,
        max = 500;
      temp.push({
        value: Math.floor(Math.random() * (max - min + 1) + min),
        color: "blue",
      });
      setArray(temp);
    }
  }
  function handleAlgoChange(e: any) {
    setAlgo(e.currentTarget.value);
    resetArray();
  }

  async function sort() {
    const arr = array;
    console.log("before : ", arr);
    switch (algo) {
      case Algorithms.bubbleSort:
        await bubbleSort(arr, setChange);
        break;
      default:
        break;
    }
  }

  return (
    <>
      <div className="nav">
        <h3>Sorting Algorithm:{algo}</h3>
        <select
          onChange={(e) => handleTypeChange(e.currentTarget.value)}
          value={type}
        ></select>
        <select onChange={handleAlgoChange}>
          {/* <option>{Algorithms.quickSort}</option>
          <option>{Algorithms.mergeSort}</option>
          <option>{Algorithms.heapSort}</option> */}
          <option>{Algorithms.bubbleSort}</option>
        </select>
        <button onClick={resetArray}>Reset Array</button>
        <button onClick={sort}>Sort</button>
      </div>
      <div className="">
        <div className="frame">
          <div className="boundary-sorting">
            {"rebuilding..."}
            {/* {console.log("rebuilding")} */}
            {array.map((e: Bar, idx) => (
              <div
                className="bar"
                key={idx}
                style={{
                  height: e.value,
                  background: e.color,
                  width: (window.innerWidth * 0.6) / size,
                }}
              ></div>
            ))}
          </div>
        </div>
      </div>
    </>
  );
}
