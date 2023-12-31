import os
import shutil
from setuptools import setup

OUTPUT_DIR = 'output'

if __name__ == "__main__":
    setup(
        name="osf_risk_model",
        packages=['osf_risk_model'],
        version="0.0.1",
        script_args=['--quiet', 'bdist_egg'], # to create egg-file only
    )

    egg_name = os.listdir('dist')[0]

    os.rename(
        os.path.join('dist', egg_name),
        os.path.join(OUTPUT_DIR, egg_name)
    )

    shutil.rmtree('build')
    shutil.rmtree('dist')
    shutil.rmtree('osf_risk_model.egg-info')
