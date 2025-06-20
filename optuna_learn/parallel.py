import optuna
from multiprocessing import Process

STUDY_NAME = "parallel_study"
STORAGE = "sqlite:///example.db"

def run_algorithm(p1, p2, p3, p4):
    # 假设这是你要调参的传统算法
    return (p1 - 3)**2 + (p2 - 0.5)**2 + (p3 - 0.01)**2 + (p4 + 5) + 0.1

def objective(trial):
    param1 = trial.suggest_int("param1", 1, 10, step=1)
    param2 = trial.suggest_float("param2", 0.0, 1.0, step=0.1)
    param3 = trial.suggest_float("param3", 1e-4, 1e-1, log=True)
    # param4 = trial.suggest_int("param4", -10, 10, step=1)
    param4 = trial.suggest_categorical("param4", [-1, -3, -4, -5])
    error = run_algorithm(param1, param2, param3, param4)
    return error

def run_worker(n_trials=100):
    study = optuna.load_study(
        study_name=STUDY_NAME,
        storage=STORAGE,
    )
    study.optimize(objective, n_trials=n_trials)
    


def main():

    # 创建 study（只做一次）
    optuna.create_study(
        study_name=STUDY_NAME,
        storage=STORAGE,
        direction="minimize",
        load_if_exists=True
    )

    # processes = []
    # NUM_WORKER = 4
    # for _ in range(NUM_WORKER):
    #     p = Process(target=run_worker)
    #     processes.append(p)

    p1 = Process(target=run_worker, kwargs={"n_trials":10})
    p2 = Process(target=run_worker, kwargs={"n_trials":100})
    p3 = Process(target=run_worker, kwargs={"n_trials":500})
    p4 = Process(target=run_worker, kwargs={"n_trials":1000})
    processes = [p1, p2, p3, p4]

    for p in processes:
        p.start()
    for p in processes:
        p.join()

    study = optuna.load_study(
        study_name=STUDY_NAME,
        storage=STORAGE,
    )
    print("Best params:", study.best_params)
    print("Best value:", study.best_value)
    print("Trials so far:", len(study.trials))



if __name__ == "__main__":
    main()